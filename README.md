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

### Edit the keywords inside `generate-writing-ideas.py`
You can specific the keywords you would like to replace [placeholder] with inside `generate-writing-ideas.py`

```
keywords = ["Lego","Python"]
```

---

### Edtiting the starter headlines template in headlines.py file
The script comes with a set of template headlines, but you can also add/edit them inside headlines.py. Just make sure to add the text [placehoder] for the spot where you would like to be replaced by your keywords.
 
For example - 

```
- "[placeholder]: Expectations vs. Reality",
- "Will [placeholder] Ever Rule the World?",
- "The Next Big Thing in [placeholder]",
- "[placeholder] Explained in Fewer than 140 Characters",
```