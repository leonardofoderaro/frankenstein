# Frankenstein
Frankenstein (Frankie, for friends) is a tool which allow you to proxy a website of your choice and modify it on the fly using a sequence of filters. 

Basic usage:

> frankie new myproject  
> cd myproject

Inside config.js specify the website you want to proxy and the chain of filters you want to apply.  

Then start frankie:

> frankie run

Point your browswer at http://0.0.0.0:5000/  

Enjoy your frankensteinaized website!

Some of the filters you can apply:

### Find and Replace some content, without parsing Html
```
{  
    "name": "first",       // the name of your choice for this filter  
    "type": "simple",      // the filter type  
    "find": "World",       // the word (or regex) you want to replace  
    "replace": "Frankie"   // the substitution to apply 
}  

```
To discover all the filters you can apply (or even how to define your own!) please take a look at the documentation.
