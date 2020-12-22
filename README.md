# Pokedex API

## Usage

 1. Build Docker image:

        $ make build # or simply `make`

 3. Start up this service:

        $ make up

 4. Open browser and link to http://localhost:5000/api/ui (API documents)

 ### Curl

 - Retrieve a Pokemon by identifier: 

        curl -X GET "http://localhost:5000/api/pokemons/1"

 - Create a Pokemon:

        curl -X POST "http://localhost:5000/api/pokemons" -H  "Content-Type: multipart/form-data" -F "name=Tentacool" -F "number=005" -F "types=Water,Poison"

      type 若不存在，會新增。

 - Update a Pokemon by identifier:

       curl -X PUT "http://localhost:5000/api/pokemons/1" -H  "Content-Type: multipart/form-data" -F "name=Bulbasaur" -F "number=011" -F "types=Gross,Poison"

 - Delete a Pokemon by identifier:

       curl -X DELETE "http://localhost:5000/api/pokemons/3"

      若刪除的是別隻神奇寶貝的進化，會出現以下訊息：

       {
         "detail": "Can not be deleted. It is an evolution of other Pokemon",
         "status": 403,
         "title": "Deletion Deined"
       }

  - Retrieve Pokemons filter by types:

        curl -X GET "http://localhost:5000/api/pokemons?type=Gross"

  - Add / Delete evolutions of Pokemon

    - Add

          curl -X PUT "http://localhost:5000/api/pokemons/1/evolutions?evolution_id=5"

    - Delete

          curl -X DELETE "http://localhost:5000/api/pokemons/1/evolutions/5"


<!--
  vi:et:wrap:ts=2:sw=2
-->
