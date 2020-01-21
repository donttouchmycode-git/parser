# parser
website scrapper for client

Project goals was to parse data of product name, price and download product picture from site with pagination.
Then save text data to csv-file, images to directory with original filenames, and save path to images for all product pictures.

Solved problems:
- some links to images was to empty file, and original path was in other tag attribute. IF-checking was implemented.
- links contained system characters and downloading did not work correctly. String correction was implemented.
- images downloaded with low resolution. Full resolution images was in other files. Replacement of part of the link was implemented.
- products was more than 1 page. Pagination parsing was implemented.
