## Trie

Trie data structure can be used to find words, given a prefix. It can be done using `O(w)`, where `w` is the length of the word.

## Use Case
- Add and search words.
- Replace words in a sentence.
- Design search autocomplete.

## Complexity

### Time

| Opeartion | Time |
|-----------|------|
| insert    | O(w) |
| search    | O(w) |
| starts_with   | O(w) |

### Space

| Opeartion | Time |
|-----------|------|
| insert    | O(1) |
| search    | O(1) |
| starts_with   | O(1) |

> **w**: length of the word of prefix   
> **n**: total no. of words  
> Total space taken will be `O(n * w)`