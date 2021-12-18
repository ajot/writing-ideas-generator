# Generate Writing Ideas
This script lets you generate ideas for writing blog articles, or Tweets. 

Sometimes, you run out of ideas to write about, or just need a bit of inspiration. Wrote a little script that does just that. 
It comes with a set of template headlines with some "placeholders" for keywords you can choose to replace with. 

## Using the script
Run the script 
```
python3 generate-writing-ideas.py
```

---

### Modifying the headlines.py file
The script comes with a set of headlines (headlines.py). For example

"[placeholder]: Expectations vs. Reality",
"Will [placeholder] Ever Rule the World?",
"The Next Big Thing in [placeholder]",
"[placeholder] Explained in Fewer than 140 Characters",


You can specific the keywords you would like to replace [placeholder] with in these template headlines.

```
#inside generate-writing-ideas.py
keywords = ["Lego","Python"]
```


You can also add/edit template headlines in headlines.py.