gorengan = "tahu bakwan risol cireng tempe mendoan gehu combro misro ubi".split(" ")
buah = "semangka jeruk mangga melon bengkoang lemon pepaya nanas srikaya sawo".split(" ")
sayur = "bayam kangkung wortel kubis brokoli kentang labu kacang melinjo genjer".split(" ")

Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)