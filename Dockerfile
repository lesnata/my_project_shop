FROM python:3.7
COPY . app/my_project_shop
WORKDIR app/my_project_shop
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python3 app.py runserver