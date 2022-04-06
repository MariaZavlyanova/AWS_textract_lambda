# AWS_textract_lambda
Augmentation au projet fil-rouge




# Les étapes à suivre pour se connecter au Bucket S3


    $ sudo apt install awscli
    $ aws configure

ID : AKIAYDZ5Q34V6N642EHA
secret acces key : (stored in secret _key.txt)

vérifier la connection :

    $ cat  ~/.aws/config
    
Vérifier que le contenu soit bon, et corrésponde à :

[default]
aws_access_key_id = <fichier zip envoyé par mail>
aws_secret_access_key = <fichier zip envoyé par mail>

# Ajouter un fichier pdf au Bucket :
il est possible de stocker temporairement le pdf dans le fichier "articles/" puis de l'envoyer sur le bucket

    $ aws s3api put-object --bucket maria-fil-rouge-s3-input --key <object key name>.pdf --body ./articles/<object key name>.pdf

# Récupérer le texte extrait du pdf :
Le texte récupéré sera stoqué dans le dossier "extracted_text/"

    $ aws s3api get-object --bucket maria-fil-rouge-s3-input --key <object key name>.txt ./extracted_text/<object key name>.txt

# Example :

    $ aws s3api put-object --bucket maria-fil-rouge-s3-input --key 2109.05504.pdf --body articles/2109.05504.pdf
    $ aws s3api get-object --bucket maria-fil-rouge-s3-input --key 1810.11936.txt ./extracted_text/1810.11936.txt
    
