# Downloading Uniprot protein sequences
## Example: Downloading a plant database of protein sequences
In order to download a large number of transcript sequences you'll have to perform uniprot "pagination". The steps are the following:

1. Go to the Uniprot website. https://www.uniprot.org/
![image](https://user-images.githubusercontent.com/25623762/228076219-69aec009-43dc-4bac-b72f-8107835e2164.png)

2. Uniprot allows you to filter sequences by going to the advanced menu and designating keywords. In this example, I filtered for taxonomy: viridiplantae and Date of creation: 07/24/2007 to current date. 

Date of creation was selected as referenced in the following website: https://www.uniprot.org/help/entries_since_rel_x

![image](https://user-images.githubusercontent.com/25623762/228077950-66d9ce2d-dde7-4602-a293-bd413e42a406.png)

3. After filtering you can use the download link or filter further using the GUI options. Additionally, you can filter for reviewed and unreviewed protein sequences.

![image](https://user-images.githubusercontent.com/25623762/228078224-5cbd1c77-be86-4765-bb02-57fc021360a6.png)

4. The download link allows you to access file formats and whether or not to compress the output with gzip compression. Here I selected for a fasta file and compression. If the request is larger than 10,000,000 sequences as seen here you'll have to generate the URL for API. Two links are given one for streaming endpoint, the other for search endpoint. In this case, we have to use the search endpoint URL and apply "pagination".

![image](https://user-images.githubusercontent.com/25623762/228078840-4e2b64dc-1d96-408b-b736-8d55ad6c2f89.png)

5. Pagination or Programmatic Pagination is defined in the following uniprot link: https://www.uniprot.org/help/pagination
In summary, it allows us to download the requested sequences in batches in order to prevent query overload. 

![image](https://user-images.githubusercontent.com/25623762/228079584-c81acf7e-30da-471d-8493-713a337d981a.png)

To begin this process you'll have to create a small bash script in order to loop through the respective download links. You can download in the Linux system using "curl". 

