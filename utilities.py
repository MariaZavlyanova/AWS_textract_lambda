import json
import spacy


# Load English tokenizer, tagger, parser and NER
try:
    nlp = spacy.load("en_core_web_md")
except: # If not present, we download
    spacy.cli.download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")


# function to add to JSON
# TODO add the verification that the pdf does not exist already
def write_json(new_data, filename, category):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[category].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)


# Create a list of references that can be found in one pdf, 
# with the url of one pdf
def extract_authors(pdf_id):
    path_pdf = "extracted_text/{}.txt".format(pdf_id)
    # Extract references from pdf_url
    # using refextract library
    with open(path_pdf) as f:
        text_content = f.read()

    # create a list where we will put all extracted authors
    authors_extracted = []


    nlp_extraction = nlp(text_content)
        # extract only the PERSON label
    list_authors_one_ref = [str(ee) for ee in nlp_extraction.ents if ee.label_ == 'PERSON']
        # store the authors in the commun list
    dic_references = {
                        "id" : "{}".format(pdf_id),
                        "list_authors" : list_authors_one_ref}

    authors_extracted.append(dic_references)

    return authors_extracted


# Store extracted list of pdf in a text file
def store_list_authors_txt(list_authors, pdf_id):
    with open("extracted_authors/{}_authors.txt".format(pdf_id), "w") as output:
        output.write(str(list_authors))

## Alimenter le JSON des references avec l'API
def create_json_referenes(pdf_id):
    extracted_reference=extract_authors(pdf_id)
    # print(extracted_reference)
    print(extracted_reference)
    write_json(extracted_reference, filename = 'authors.json', category = 'Authors')

