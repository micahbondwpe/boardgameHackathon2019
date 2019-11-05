curl -s https://api.geekdo.com/xmlapi/boardgame/1 | perl -n -e '/<playingtime>(.*)<\/playingtime>/ && print $1'

curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<boardgame objectid' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<name primary="true"' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<minplayers>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<maxplayers>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<playingtime>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<age>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<boardgamecategory>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<boardgamemechanic>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<image>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<thumbnail>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'
curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep '<average>' | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'


\"$(grep '<name primary="true"' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\"
$(grep '<minplayers>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')
$(grep '<maxplayers>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')
$(grep '<playingtime>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')
$(grep '<age>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')
\"$(grep '<boardgamecategory' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}' | tr '\n' ',' | rev | cut -c 2- | rev)\"
\"$(grep '<boardgamemechanic' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}' | tr '\n' ',' | rev | cut -c 2- | rev)\"
\"$(grep '<image>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\"
\"$(grep '<thumbnail>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\"
$(grep '<average>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')



curl -s https://api.geekdo.com/xmlapi/boardgame/1 | grep -E '<boardgame objectid|<name primary="true"|<minplayers>|<maxplayers>|<playingtime>|<age>|<boardgamecategory|<boardgamemechanic'

curl -s https://api.geekdo.com/xmlapi/boardgame/1?stats=1 | grep -E '<boardgame objectid|<name primary="true"|<minplayers>|<maxplayers>|<playingtime>|<age>|<boardgamecategory|<boardgamemechanic|<average>|<image>|<thumbnail>' > $i.xml

for i in {1..100} ; do curl -s https://api.geekdo.com/xmlapi/boardgame/$i.xml?stats=1 | grep -E '<boardgame objectid|<name primary="true"|<minplayers>|<maxplayers>|<playingtime>|<age>|<boardgamecategory|<boardgamemechanic|<average>|<image>|<thumbnail>' > $i.xml.xml ; done


INSERT INTO <table name> (id,name,image,thumbnail,boardgamecategory,boardgamemechanic,age,minplayers,maxplayers,playingtime,rating)

echo { \"id\": $(grep '<boardgame objectid=' ../xml/$i.xml | awk -F '"' '{print $2}'), \"name\": \"$(grep '<name primary="true"' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\", \"image\": \"$(grep '<image>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\", \"thumbnail\": \"$(grep '<thumbnail>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\", \"


for i in {1..3000}; do echo { \"id\": $(grep '<boardgame objectid=' ../xml/$i.xml | awk -F '"' '{print $2}'), \"name\": \"$(grep '<name primary="true"' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\", \"minplayers\": $(grep '<minplayers>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'), \"maxplayers\": $(grep '<maxplayers>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'), \"playingtime\": $(grep '<playingtime>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'), \"age\": $(grep '<age>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'), \"boardgamecategory\": \"$(grep '<boardgamecategory' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}' | tr '\n' ',' | rev | cut -c 2- | rev)\", \"boardgamemechanic\": \"$(grep '<boardgamemechanic' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}' | tr '\n' ',' | rev | cut -c 2- | rev)\", \"rating\": $(grep '<average>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}'), \"image\": \"$(grep '<image>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\", \"thumbnail\": \"$(grep '<thumbnail>' ../xml/$i.xml | awk -F '>' ' {print $2}' | awk -F '<' '{print $1}')\" } | head -n1 > $i.json ; echo "done $i.json" ; done
