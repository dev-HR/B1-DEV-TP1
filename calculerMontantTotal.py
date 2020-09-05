#!/usr/bin/python3

FRAIS_LIVRAISON = 3.5

numCommande = 19234

nomClient = "Capliez"

print( "Commande numéro" , numCommande )

print( "\tpassée par le client" , nomClient , "\n")

montantResto = input( "Saisir le montant : " )

montantResto = float( montantResto )

montantTotal = montantResto + FRAIS_LIVRAISON

print( "\nLe client" , nomClient  , end = " " )

print( "a commandé pour un montant de" ,  montantTotal , "€." )
