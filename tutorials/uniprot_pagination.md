# Downloading Uniprot Protein Sequences

## Example: Downloading a Plant Database of Protein Sequences

To download a large number of protein sequences from Uniprot, you'll need to perform "pagination". Here are the steps:

1. Go to the [Uniprot website](https://www.uniprot.org/).

   ![Uniprot website](https://user-images.githubusercontent.com/25623762/228076219-69aec009-43dc-4bac-b72f-8107835e2164.png)

2. Use the advanced search options to filter the sequences. In this example, let's filter for taxonomy: Viridiplantae and Date of creation: 07/24/2007 to the current date.

   ![Uniprot advanced search](https://user-images.githubusercontent.com/25623762/228077950-66d9ce2d-dde7-4602-a293-bd413e42a406.png)

3. After filtering, you can further refine the results using the GUI options. Additionally, you can choose to filter for reviewed and unreviewed protein sequences.

   ![Uniprot filter options](https://user-images.githubusercontent.com/25623762/228078224-5cbd1c77-be86-4765-bb02-57fc021360a6.png)

4. The download link provides options for file formats and compression. In this example, select the FASTA format with compression. If the request is larger than 10,000,000 sequences, you'll need to generate the URL for the API. Two links are provided, one for the streaming endpoint and the other for the search endpoint. For pagination, you need to use the search endpoint URL.

   ![Uniprot download options](https://user-images.githubusercontent.com/25623762/228078840-4e2b64dc-1d96-408b-b736-8d55ad6c2f89.png)

5. Pagination or Programmatic Pagination is explained in the [Uniprot documentation](https://www.uniprot.org/help/pagination). It allows you to download the requested sequences in batches to prevent query overload.

   ![Uniprot pagination](https://user-images.githubusercontent.com/25623762/228079584-c81acf7e-30da-471d-8493-713a337d981a.png)

To begin the process, create a small Bash script to loop through the respective download links. You can use `curl` command in a Linux system to perform the downloads.

[Back to Table of Contents](README.md#table-of-contents)
