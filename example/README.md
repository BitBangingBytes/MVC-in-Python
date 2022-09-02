# MVC in Python

## Application execution
This example differs from the original in that it uses a new CustomersLocal.py file for the model. 
It uses a list of lists to keep track of uses instead of SQL, no nothing other than this sample code is needed
to execute the example.

You can ignore the instructions below, they are left here so you can see how the original example worked.

<hr />


If you want to execute the application to see how it works, you have to download the database file that the app uses. 
This file is in <code>db/mvc.sql</code>. After that, it's necessary to load the file in a server (local or online) with 
support to MySQL database. I executed the app using a local server (as I use Windows, I used "Wampp" to make a local 
server, but if you use another operational system, there are other similar softwares, like Xampp [for Linux] or 
Mamp [for Mac]).

Furthermore, the app use "mysql connector" library; if you don't have it, it's necessary install it.
### Links
- [mysql connector](https://pypi.org/project/mysql-connector-python/)
- [Wampp](http://www.wampserver.com/en/)
- [Mamp](https://www.mamp.info/)
- [Xampp](https://www.apachefriends.org/pt_br/index.html)

<hr />

## Application photos
#### Inicial window
![Inicial window (Home)](
https://github.com/BitBangingBytes/MVC-in-Python/blob/master/media/example/home.PNG?raw=true)

#### Show window
![Show window (if you run the app, try to click with the mouse right button on a row))](
https://github.com/BitBangingBytes/MVC-in-Python/blob/master/media/example/showTreeView.PNG?raw=true)

#### Another show window without TreeView
![Another show window without TreeView widget](
https://github.com/BitBangingBytes/MVC-in-Python/blob/master/media/example/show.PNG?raw=true)
<hr>
