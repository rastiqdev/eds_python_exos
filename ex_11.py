f = open("ex_11_test.txt", "w")
f.write("Louis Licari")
f.close()

f = open("ex_11_test.txt", "r")
print(f.read())