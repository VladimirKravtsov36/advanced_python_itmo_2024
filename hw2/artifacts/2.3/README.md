## Запуск
```
docker build . -t python-latex
docker run -it --rm --name to-latex -v $PWD:/home/code -w /home/code python-latex python create_pdf_file.py
```