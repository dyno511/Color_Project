@echo off
title Update


echo "----------Update Code----------"
python UpdateAPP.py
echo "----------END Update Code----------"


echo "----------Update Library----------"
pip install -r ./APP_Color_Project/requirements.txt
echo "----------END Update Library----------"


