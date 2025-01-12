from flask import Flask, request, jsonify
import numpy as np
app = Flask(_name_)

#DATA STIMULATION

ratings =  [
  {"userID" : "user1", "courseID": "Course_A", "Rating": 5},
  {"userID" : "user1", "courseID": "Course_B", "Rating": 4},
  {"userID" : "user2", "courseID": "Course_A", "Rating": 3},
  {"userID" : "user2", "courseID": "Course_C", "Rating": 4},
