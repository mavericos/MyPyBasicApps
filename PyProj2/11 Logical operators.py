print((10 > 5)
      and (1 < 3)
      and "A" == "c")

# and само ако всички са верни - True иначе False

print((10 > 15)
      or (10 < 3)
      or "A" == "A")

# or само ако всички са грешни - False иначе True

print(10 < 5
    or 1 < 3  # задължително едното ИЛИ да е True
      and "A" == "A") # И задължително а == а за True

print(not("Ivan" == "Stanka"))  #true
print("Ivan" == "Stanka")   #false

