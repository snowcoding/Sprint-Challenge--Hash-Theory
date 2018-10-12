import re
# * The VT-100 terminal (console) outputs text to the screen as it
#   receives it over the wire. One exception is that when it receives an
#   ESC character (ASCII 27), it goes into a special mode where it looks
#   for commands to change its behavior. For example:

#       ESC[12;45f

#   moves the cursor to line 12, column 45.

#       ESC[1m

#   changes the font to bold.

#   * Come up with regexes for the two above sequences. The one to set the
#     cursor position should accept any digits for the row and column. The
#     bold sequence need only accept `1` (and is a trivial regex). (ESC is
#     a single character which can be represented with `\e` in the regex.)


line1 = 'ESC[12;45f'
line2 = '1999-1-20'

print("\nRegex XY coord:")
match1 = re.match('ESC\[[0-9]{1,2}\;[0-9]{1,2}f', line1)
match2 = re.match('ESC\[[0-9]{1,2}\;[0-9]{1,2}f', line2)
print (f"testing {line1}: {match1.group()}" )
print (f"testing {line2}: {match2}" )