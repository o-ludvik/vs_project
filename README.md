# vs_project
Máme problém s naším projektem, nechce projít pytest na githubu. Myslím si že problém je v příkazu Run pytest --doctest-modules --cov=. --cov-fail-under=66 *.
Zkoušel jsem to na svojí mašině a hodilo mi to error že to nebere user input a mám tam přidat -s, po přidání -s to prošlo pytest na 86% bez problému a i flake8.
