meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
    
while True:  
    secim = input("eklemek için e, sormak için s, çıkmak için q giriniz")
    
    if secim == "q":
        print("çıkılıyor...")
        break
    
    elif secim == "e":
        key = input("Kelimeyi büyük harf giriniz = ")
        value = input("Kelimenin anlamını giriniz = ")
        if key not in meme_dict.keys():
            meme_dict[key] = value
            
    elif secim == "s":
        
        word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!):")
        
        
        if word in meme_dict.keys():
            # Kelime eşleşiyorsa ne yapmalıyız?
            print(meme_dict[word])
        else:
            # Kelime eşleşmiyorsa ne yapmalıyız?
            print("Sözlükte bu kelime bulunmamaktadır.")
    
    else:
        print("Hatalı giriş yaptınız")

