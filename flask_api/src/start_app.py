'''
Created on Nov 16, 2020

@author: apratim
'''
import all_api

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    all_api.app.run(threaded=True, port=9800)