# InjamTanvir(INJAM UL HAQUE)

import re
x = 'We just received $10.00 for cookies.$23.00'
y = re.findall('\$[0-9.]+', x)  # \$[0-9.]+ will match a dollar sign followed by one or more digits or periods, which is useful for extracting monetary amounts.
print(y)
