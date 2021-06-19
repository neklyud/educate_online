#!/bin/bash

pytest tests/*
if [ $? -eq 0 ];
then
    uvicorn main:app --host 0.0.0.0 --reload --port 5000
else
    echo 'Tests failure'
fi