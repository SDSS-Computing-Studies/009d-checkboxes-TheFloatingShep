#! python3

import task1
import tkinter as tk
from tkinter import *

def test1():
  test = task1.binary_to_decimal( (0,0,0,1,1,0,0,1) )
  assert test == 25

def test2():
  test = task1.decimal_to_binary( 50 )
  assert test == (0,0,1,1,0,0,1,0)