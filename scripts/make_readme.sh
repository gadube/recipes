#!/bin/bash -e

THIS_DIR=$(dirname $0)

echo "" > "$THIS_DIR/../README.md"
while IFS= read -r LINE; do
  # Process each line here
  echo "$LINE" >> "$THIS_DIR/../README.md"
done < $THIS_DIR/../templates/README.template.md

FILE_LIST=$(find $THIS_DIR/../src -type f)

echo "" >> "$THIS_DIR/../README.md"
echo "" >> "$THIS_DIR/../README.md"

for FILE in $FILE_LIST
do 
  BASENAME=$(basename $FILE)
  FILE_WITHOUT_EXTENSION=${BASENAME%.md}
  DISPLAY_NAME=${FILE_WITHOUT_EXTENSION//-/ }

  CAPITALIZED_DISPLAY_NAME=""
  for word in $DISPLAY_NAME; 
  do 
    INTERMEDIATE_DISPLAY_NAME=`echo "${word:0:1}" | tr "[:lower:]" "[:upper:]"`
    CAPITALIZED_DISPLAY_NAME="${CAPITALIZED_DISPLAY_NAME}${INTERMEDIATE_DISPLAY_NAME}${word:1} "
  done

  CAPITALIZED_DISPLAY_NAME=`echo $CAPITALIZED_DISPLAY_NAME | xargs`
  echo "- [$CAPITALIZED_DISPLAY_NAME]($FILE)" >> "$THIS_DIR/../README.md"
done
