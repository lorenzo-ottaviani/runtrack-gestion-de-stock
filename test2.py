import customtkinter as ctk

# Simuler une base de données avec un dictionnaire
product_db = {
    1: {"name": "Pomme", "stock": 28, "price": 3.50},
    2: {"name": "Banane", "stock": 35, "price": 2.00},
    3: {"name": "Orange", "stock": 50, "price": 2.50},
    4: {"name": "Poire", "stock": 20, "price": 3.00}
}


# Fonction pour gérer les actions des boutons
def on_button_click(button_text):
    if button_text == "Read product informations":
        # Afficher la zone de saisie pour l'ID du produit et le bouton de recherche
        id_label.grid(row=2, column=0, padx=10, pady=5)
        id_entry.grid(row=2, column=1, padx=10, pady=5)
        search_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Cacher le label des résultats s'il est déjà affiché
        result_label.grid_forget()

    else:
        # Cacher la zone de saisie et le bouton de recherche pour les autres boutons
        id_label.grid_forget()
        id_entry.grid_forget()
        search_button.grid_forget()

        # Afficher le texte du bouton cliqué dans le label de résultat
        result_label.configure(text=f"{button_text} clicked")
        result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


def search_product():
    try:
        # Récupérer l'ID saisi par l'utilisateur
        product_id = int(id_entry.get())
        # Chercher le produit dans la base de données
        if product_id in product_db:
            product = product_db[product_id]
            product_info = f"Produit: {product['name']} | Nombre en stock: {product['stock']} | Prix à l'unité: {product['price']}€"
            result_label.configure(text=product_info)  # Afficher le résultat
        else:
            result_label.configure(text="Produit introuvable.")

        # Cacher la zone de saisie de l'ID et le bouton de recherche, puis afficher le résultat
        id_label.grid_forget()
        id_entry.grid_forget()
        search_button.grid_forget()

        # Afficher le résultat dans la zone de résultat
        result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    except ValueError:
        result_label.configure(text="Veuillez entrer un ID valide.")
        # Cacher la zone de saisie de l'ID et le bouton de recherche, puis afficher le message d'erreur
        id_label.grid_forget()
        id_entry.grid_forget()
        search_button.grid_forget()

        # Afficher le message d'erreur dans la zone de résultat
        result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Créer la fenêtre principale
root = ctk.CTk()
root.title("Store Manager")
root.geometry("900x600")

# Titre en haut de la fenêtre
title_label = ctk.CTkLabel(root, text="STORE MANAGER", font=("Helvetica", 32))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Créer un cadre pour les boutons
button_frame = ctk.CTkFrame(root)
button_frame.grid(row=1, column=0, columnspan=2, pady=30)

# Boutons pour les différentes actions
create_button = ctk.CTkButton(button_frame, text="CREATE A NEW PRODUCT", font=("Helvetica", 20, "bold"),
                              width=400, height=100, fg_color="#4CAF50", hover_color="#45a049",
                              command=lambda: on_button_click("Create a new product"))
create_button.grid(row=0, column=0, padx=20, pady=10)

update_button = ctk.CTkButton(button_frame, text="UPDATE A PRODUCT", font=("Helvetica", 20, "bold"),
                              width=400, height=100, fg_color="#FF9800", hover_color="#fb8c00",
                              command=lambda: on_button_click("Update a product"))
update_button.grid(row=0, column=1, padx=20, pady=10)

read_button = ctk.CTkButton(button_frame, text="READ PRODUCT INFORMATIONS", font=("Helvetica", 20, "bold"),
                            width=400, height=100, fg_color="#2196F3", hover_color="#1976D2",
                            command=lambda: on_button_click("Read product informations"))
read_button.grid(row=1, column=0, padx=20, pady=10)

delete_button = ctk.CTkButton(button_frame, text="DELETE A PRODUCT", font=("Helvetica", 20, "bold"),
                              width=400, height=100, fg_color="#F44336", hover_color="#e53935",
                              command=lambda: on_button_click("Delete a product"))
delete_button.grid(row=1, column=1, padx=20, pady=10)

# Zone en bas pour les inputs de l'utilisateur et l'affichage des résultats
id_label = ctk.CTkLabel(root, text="Enter Product ID:")
id_entry = ctk.CTkEntry(root, width=250)
search_button = ctk.CTkButton(root, text="Search", command=search_product)

# Label pour afficher le résultat (information du produit)
result_label = ctk.CTkLabel(root, text="", font=("Helvetica", 14))

# Lancer l'application
root.mainloop()
