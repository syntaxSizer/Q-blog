# How to Embed google map

### steps to embed responsive google map in your web page


Embeding google map is simple as eating cake on a weekend , hover the defualt google map is't responsive .
in other word you won't be able to view the full map on smaller screens such as smart phones etc, you will have to scroll to view the areas covered by the map
To emped google map you need to follow two simple steps .
whie you are in google maps zoom in the location you want to embed
click on share button on your left side see picture


![image](/images/screenshot1.png)

The next step is to copy the link from the window that will pop up after you click the share button.  Paste the link in your web page.

![image](/images/Screenshot2.png)

Thats how you Embed a google map in your web page.

next we will go through how to make that map responsive, by that i mean to make the map resize according to the size of the screen

to achive this we will have to put some css lines of code , but it's not a big deal
create a 'div' to warp the map link and give it a class name let's say google-map
apply this CSS to google-map class

map responsiveness code

```
.google-map {
            position: relative;  /* note the position of the warpper must be relative
            padding-bottom: 75%; /* This is the aspect ratio*/
            height: 0;
            overflow: hidden;
        }
        ```
Note google-map most be the warpper class of the map
next we need to apply some code to the content of google-map class and it's the iframe tag


```
.google-map iframe {
            position: absolute; while here it should be absolute
            top: 0;
            left: 0;
            width: 100% ;
            height: 100% ;
        }
        ```

Thats all enjoy a respnsive google map in your web page
