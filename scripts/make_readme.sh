#!/bin/bash -e

README_CONTENTS=$(cat ../templates/README.md)

FILE_LIST=$(ls -lt1 ../recipes)

echo $README_CONTENTS >> ../README.md
echo "" >> ../README.md
echo "" >> ../README.md

for FILE in $FILE_LIST
do 
  FILE_WITHOUT_EXTENSION=${FILE%.md}
  DISPLAY_NAME=${FILE_WITHOUT_EXTENSION//-/ }

  CAPITALIZED_DISPLAY_NAME=""
  for word in $DISPLAY_NAME; 
  do 
    INTERMEDIATE_DISPLAY_NAME=`echo "${word:0:1}" | tr "[:lower:]" "[:upper:]"`
    CAPITALIZED_DISPLAY_NAME="${CAPITALIZED_DISPLAY_NAME}${INTERMEDIATE_DISPLAY_NAME}${word:1} "
  done

  CAPITALIZED_DISPLAY_NAME=`echo $CAPITALIZED_DISPLAY_NAME | xargs`
  echo "($CAPITALIZED_DISPLAY_NAME)[$FILE]" >> ../README.md
done
