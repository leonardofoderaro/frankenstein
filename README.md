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

### Simple  
find and replace some content, without parsing Html
```
{  
    "name": "first",       // the name of your choice for this filter  
    "type": "simple",      // the filter type  
    "find": "World",       // the word (or regex) you want to replace  
    "replace": "Frankie"   // the substitution to apply 
}  
```  

### XPathRemove  
find an element using XPath, then clear it
```  
{
    "name": "drop_login_box",  // the name for this filter
    "type": "XPathRemove",     // filter type
    "xpath": "//div[@id=\"head_right\"]"  // element(s) to be cleared
}
```  

### InjectRemoteJS  
inject a <script src="..."></script> node inside the head section
```
{
    "name": "inject_vue_js",    // filter name
    "type": "InjectRemoteJS",   // filter type
    "url": "https://cdn.jsdelivr.net/npm/vue/dist/vue.js"  // the remote script to load, in this case Vue.js
}
```

### XPathSetText  
finds an element using an XPath expression, then set its text property
```
{
    "name": "set_footer",    // filter name
    "type": "XPathSetText",  // filter type
    "find": "//span[@class=\"site-footer-credits\"]",  // element to find
    "text": "Proudly patched by <a href=\"https://github.com/leonardofoderaro/frankie\">frankie</a>."  // content to be used as text property
}
```


### XPathCopyFromRemote  
selects an element from a remote document and inject it at the specified location
```
{
    "name": "add_tagline",    // filter name
    "type": "XPathCopyFromRemote",  // filter type
    "origin": "https://github.com/leonardofoderaro/frankie",   // the remote document with the element to be injected
    "XPathSource": "//div[@id=\"readme\"]/article/p[1]",       // the location of the element to be injected
    "XPathDest": "//h2[@class=\"project-tagline\"]"            // where it must be inserted in the local document
},
```


