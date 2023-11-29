# NOTES
## Dissect Description
### Considerations
Linebreaks
- May be done using \n
- Or, may be done using \<br> and have extraneous HTML characters

Apostrophe's
- May be denoted using some odd ampersand symbolism

"Additional Information"
- May instead be spelt "Additional information"
- May be mispelled by a character or two
- May not be included at all

### Method
1. Clean white spaces around description using `.strip()`
2. Extract demonstrations data. Depends on how line breaking works
3. Extract additional information data