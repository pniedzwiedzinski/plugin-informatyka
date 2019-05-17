function informatyka -d "My package"
  cd /Users/pniedzwiedzinski/Documents/Projekty/informatyka
  echo "git --git-dir=/Users/pniedzwiedzinski/.informatyka/git status -u | grep '.cpp\|.xlsx' | zip inf \$(cat)" | bash
  mv inf.zip /Users/pniedzwiedzinski/.informatyka
  
  cd /Users/pniedzwiedzinski/.informatyka
  pipenv run main.py
  cd /Users/pniedzwiedzinski/Documents/Projekty/informatyka
  
  git --git-dir=/Users/pniedzwiedzinski/.informatyka/git add .
  git --git-dir=/Users/pniedzwiedzinski/.informatyka/git commit -m "Informatyka - dodano automatycznie"
  git --git-dir=/Users/pniedzwiedzinski/.informatyka/git push
end
