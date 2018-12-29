"""
Ascii-art fireworks.
"""


_fw1 = r"""
    .\'/. 
   -= o =-
   .'/-\'.
    .     
   .      
  .       
"""


kaboom = """
            \033[41m KABOOM! \033[0m
"""

def _mult(fw, n, space="  "):
    "Repeat a firework n times, horizontally."
    lines = fw.split('\n')
    nlines = []
    for line in lines:
        nlines.append( space.join([line]*n) )
    return "\n".join(nlines)

fireworks = [_mult(_fw1,i) for i in range(6)]
