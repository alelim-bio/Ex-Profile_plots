# Ex-Profile_plots
Examples on creating profile plots.

## Example 1: Creating a profile(density/histogram) plot across all genes in a dataset based on their regions e.g. 5' UTR, CDS, 3' UTR.
 - The raw dataset should be a table of values where the rows represent each gene and the columns are the values that are associated with the gene. 
 - For this example we will start off with a table of genes that have values associated with basepair position.

### An example for a gene with a length of 1,000 bp: 
|GENE IDs        |val 1|val 2|val 3|val 4|val 5|val 6|val 7|val 8|val 9|
|:--------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gene_1         | 25  | 30  | 50  | 150 | 250 | 500 | 750 | 850 | 925 |

 - This assumes a 1-based coordinate system for each transcript.
 - Each value a the position of the detected modification.
 - In this case we will know the CDS start and end positions. 
 - This example will have 200 to 800 be the represented CDS start and positions. This means that:
  -  1 to 200 will be in the 5' UTR group
  -  201 to 800 will be in the CDS group
  -  801 to 1,000 will be in the 3' UTR group
 - Now we will classify all values between these groups into their respective regions.
```python
mod_dataframe

def ClassifyRegionValues():
 
```
- After classifying regions we will transform the values to be relative to their overall length of their region. 
- In order to do this we will take each value that's in their respective group adjust the positions to start at 1 and divide it by the group length. 
#### 5' UTR Example: Length = 200
  - **Since the 5' UTR starts from 1 we don't have to adjust the positions.**
  
| REGION |val 1|val 2|val 3|val 4|
|:------:|:---:|:---:|:---:|:---:|
| 5' UTR | 25  | 30  | 50  | 150 |

  - **Eq:** Position divided by group length.
    * 25 / 200 = 0.125
    * 30 / 200 = 0.15
    * 50 / 200 = 0.25
    * 150 / 200 = 0.75
  
| REGION | val 1 | val 2 | val 3| val 4|
|:------:|:-----:|:-----:|:----:|:----:|
| 5' UTR | 0.125 | 0.150 | 0.25 | 0.75 |

#### CDS Example: Length = 600
| REGION | val 1 | val 2 | val 3|
|:------:|:-----:|:-----:|:----:|
| CDS    | 250   | 500   | 750  |

 - **Eq:** (Position - 5' UTR length) / CDS length
   * (250 - 200) / 600 = 0.0833
   * (500 - 200) / 600 = 0.5
   * (750 - 200) / 600 = 0.9166

| REGION | val 1  | val 2 | val 3 |
|:------:|:------:|:-----:|:-----:|
| CDS    | 0.0833 | 0.5   | 0.9166|

#### 3' UTR Example: Length = 200
| REGION | val 1 | val 2 | val 3 |
|:------:|:-----:|:-----:|:-----:|
| 3' UTR | 25    | 30    | 50    |

 - **Eq:** (Position - (5' UTR length + CDS length)) / 3' UTR length
   * (850 - 800) / 200 = 0.25
   * (925 - 800) / 200 = 0.625

| REGION | val 1 | val 2 | 
|:------:|:-----:|:-----:|
| 3' UTR | 0.25  | 0.625 | 

#### Merge transformed gene regions
 - After each individual group has it's values transformed, we will adjust the values to be representative of their position relative to the overall gene structure e.g. 5' UTR - CDS - 3' UTR.
 - To do so we understand that each region is a value between 0 to 1. This allows us to adjust the values by these scalars.
 - Then we will merge all values into a list to be a single gene representation.

 - 5' UTR stays in the front so none of these values are changed.

 | REGION | val 1 | val 2 | val 3| val 4|
 |:------:|:-----:|:-----:|:----:|:----:|
 | 5' UTR | 0.125 | 0.150 | 0.25 | 0.75 |

- The CDS values is transformed by adding 1 to all values.

| REGION | val 1  | val 2 | val 3  |
|:------:|:------:|:-----:|:------:|
| CDS    | 1.0833 | 1.5   | 1.9166 |

- The 3' UTR is transformed by adding 2 to all values.

| REGION | val 1 | val 2 | 
|:------:|:-----:|:-----:|
| 3' UTR | 2.25  | 2.625 | 

- Following this we will merge them into a single gene representation.

- **BEFORE**

|GENE IDs        | val 1 | val 2 | val 3| val 4| val 5  |val 6| val 7  | val 8| val 9 |
|:--------------:|:-----:|:-----:|:----:|:----:|:------:|:---:|:------:|:----:|:-----:|
| gene_1         | 25    | 30    | 50   | 150  | 250    | 500 | 750    | 850  | 925   |

- **AFTER**

|GENE IDs        | val 1 | val 2 | val 3| val 4| val 5  |val 6| val 7  | val 8| val 9 |
|:--------------:|:-----:|:-----:|:----:|:----:|:------:|:---:|:------:|:----:|:-----:|
| gene_1         | 0.125 | 0.150 | 0.25 | 0.75 | 1.0833 | 1.5 | 1.9166 | 2.25 | 2.625 |

 - This will be applied to all the genes to create a new dataset.

```python
mod_dataframe

def TransformValues(mod_dataframe):
  
```

### Create a profile plot by using either a histogram of density plot
 - With the new dataset we can create a profile plot using a library or package of your choice.


#### Example python code to randomly generate a matrix to create a density plot with seaborn
```python
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def generate_random_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            if random.random() < 0.5:
                # Known distribution
                value = np.random.choice([0.2, 1.5, 2.8], p=[0.3, 0.4, 0.3])
            else:
                # Unknown random value
                value = random.uniform(0, 3)
            value = max(0, min(3, value))  # Ensure value is within range
            row.append(value)
        matrix.append(row)
    return matrix

rows = 1000
columns = 15

random_matrix = generate_random_matrix(rows, columns)

# Convert the matrix to a flat list
values = [value for row in random_matrix for value in row]

# Define the category boundaries
boundary_1 = 1
boundary_2 = 2

# Plot the density plot
sns.kdeplot(values)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Plot')

# Draw shaded regions for the categories
plt.gca().add_patch(Rectangle((0, 0), boundary_1, 1, facecolor='red', alpha=0.2, label="5' UTR"))
plt.gca().add_patch(Rectangle((boundary_1, 0), boundary_2 - boundary_1, 1, facecolor='green', alpha=0.2, label="CDS Region"))
plt.gca().add_patch(Rectangle((boundary_2, 0), 3 - boundary_2, 1, facecolor='blue', alpha=0.2, label="3' UTR"))

# Set x-axis limits
plt.xlim(0, 3)

plt.legend()

# Save the plot as a PDF file
plt.savefig('density_plot.pdf')

```
