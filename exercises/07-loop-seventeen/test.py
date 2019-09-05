import io
import sys
sys.stdout = buffer = io.StringIO()


from app import numb
import pytest

