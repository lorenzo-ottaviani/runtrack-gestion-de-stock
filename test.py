import customtkinter as ctk

# Fonction pour gérer les actions des boutons
def on_button_click(button_text):
    print(f"Button clicked: {button_text}")
    # Tu peux ajouter des comportements ici selon le bouton cliqué

# Créer la fenêtre principale
root = ctk.CTk()
root.title("Store Manager")
root.geometry("900x600")

# Titre en haut de la fenêtre
title_label = ctk.CTkLabel(root, text="STORE MANAGER", font=("Helvetica", 32))
title_label.pack(pady=20)

# Créer un cadre pour les boutons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=30)

# Boutons pour les différentes actions
create_button = ctk.CTkButton(button_frame, text="CREATE A NEW PRODUCT", font=("Helvetica", 20, "bold"),
                              width=400, height=100, fg_color="#4CAF50",  hover_color="#45a049",
                              command=lambda: on_button_click("Create a new product"))
create_button.grid(row=0, column=0, padx=20, pady=10)

update_button = ctk.CTkButton(button_frame, text="UPDATE A PRODUCT", font=("Helvetica", 20, "bold"),
                              width=400, height=100, fg_color="#FF9800",  hover_color="#fb8c00",
                              command=lambda: on_button_click("Update a product"))
update_button.grid(row=0, column=1, padx=20, pady=10)

read_button = ctk.CTkButton(button_frame, text="READ PRODUCT INFORMATIONS", font=("Helvetica", 20, "bold"),
                            width=400, height=100, fg_color="#2196F3",  hover_color="#1976D2",
                            command=lambda: on_button_click("Read product informations"))
read_button.grid(row=1, column=0, padx=20, pady=10)

delete_button = ctk.CTkButton(button_frame, text="DELETE A PRODUCT", font=("Helvetica", 20, "bold"),
                              width=400, height=100, fg_color="#F44336",  hover_color="#e53935",
                              command=lambda: on_button_click("Delete a product"))
delete_button.grid(row=1, column=1, padx=20, pady=10)

# Zone en bas pour les inputs de l'utilisateur
input_frame = ctk.CTkFrame(root)
input_frame.pack(side="bottom", fill="x", padx=20, pady=30)

# Par exemple, un champ de texte pour créer un produit
product_name_label = ctk.CTkLabel(input_frame, text="Product Name:")
product_name_label.grid(row=0, column=0, padx=10, pady=5)

product_name_entry = ctk.CTkEntry(input_frame, width=250)
product_name_entry.grid(row=0, column=1, padx=10, pady=5)

product_price_label = ctk.CTkLabel(input_frame, text="Product Price:")
product_price_label.grid(row=1, column=0, padx=10, pady=5)

product_price_entry = ctk.CTkEntry(input_frame, width=250)
product_price_entry.grid(row=1, column=1, padx=10, pady=5)

# Lancer l'application
root.mainloop()
