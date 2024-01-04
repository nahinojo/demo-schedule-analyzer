export const camelToTitleCase = (camelString: string): string => {
  let titleString = camelString[0].toUpperCase()
  let i = 1
  while (i < camelString.length) {
    const char = camelString[i]
    if (char !== char.toUpperCase()) {
      titleString = ''.concat(
        titleString, char
      )
    } else {
      titleString = ''.concat(
        titleString, ' ', char
      )
    }
    i++
  }
  return titleString
}
