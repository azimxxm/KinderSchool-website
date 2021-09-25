## KinderSchool-website

* <a href="#Mobile">Mobile verion view</a>

* <a href="#Desktop">Desktop verion view</a>
<a id="home"></a>
* __info__
Today, great conditions are being created for the education of our future youth. Private kindergartens and schools are also opening My job is to create a website for a private kindergarten, I created it using __HTML CSS JavaScript Python__. Its back was in the Django frame of the Python programming language library

__Contact me if you need a website or app!__

> __Technologies used in the program__
>
>* __HTML__
>* __CSS__
>* __JavaScriptL__
>* __Python__
>* __Django__
>* __Postgresql__ or __SQLite3__
>

__You can change the locations you want from the models.py section__

```python

class Teachers(models.Model):
    name = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)
    telegram_url = models.URLField(blank=True)
    imstagram_url = models.URLField(blank=True)
    likedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="Teachers/%Y/%m/")

    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.name
```

## Instructions for use

``` bash
# First you download the project zip file from github and unzip it and call it from the archive

# You run the file through the terminal pip install -r requirements.txt
pip install -r requirements.txt

# Step 1
py manage.py makemigrations

# Step 2
py manage.py migrate 

# Step 3
py manage.py createsuperuser


# Step 4
py manage.py runserver

# Your result will appear in the web browser via http://127.0.0.1:8000/

```
<div id="Desktop"></div>

### Home page 

![home](https://user-images.githubusercontent.com/76002783/134764304-cece735f-64ca-48a5-9220-0c91dd93b0c2.PNG)

### Class page 

![class blog](https://user-images.githubusercontent.com/76002783/134764330-3bc3a03c-5224-4a62-85c5-25bb78b8a81b.PNG)

### About page 

![about](https://user-images.githubusercontent.com/76002783/134764317-cca8ab6f-1987-4dc4-ae07-5e28acabeff9.PNG)

### Contact page 

![contact](https://user-images.githubusercontent.com/76002783/134764333-a4611341-e6ed-4351-89fe-e35b4a81f68b.PNG)

### Admin panel 

![admin](https://user-images.githubusercontent.com/76002783/134764329-76bb5227-bf71-4e83-b1bd-4b53397e67ab.PNG)


### Teacher viewing panel

![o'qituvchi admin](https://user-images.githubusercontent.com/76002783/134764316-6f4a64c5-cf3f-476d-91ca-64e1be103d7a.PNG)


### Mobile version
<div id="Mobile"></div>

![mobile 1](https://user-images.githubusercontent.com/76002783/134766035-f5d1ad6b-0591-4931-aeff-cf595ac86140.PNG) | ![mobile 2](https://user-images.githubusercontent.com/76002783/134766038-5b014961-a350-4a5a-aec2-e1a4f460a62e.PNG) | ![mobile 3](https://user-images.githubusercontent.com/76002783/134766042-df0fc825-4b87-4a6f-9b06-e2ddba962c75.PNG) | ![mobile](https://user-images.githubusercontent.com/76002783/134766044-367e1f6b-3f36-4072-b184-cfce4c7d0cdb.PNG)

* <a href="#home">⬆️</a>
