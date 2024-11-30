from hashlib import *
import rsa
import os
import sys
from base64 import *

def h1(litterlist, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = l1
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h2(nn, k10, sp, ep, f)

def h2(litterlist, h1, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h1
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h3(nn, k10, sp, ep, f)
    
def h3(litterlist, h2, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h2
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h4(nn, k10, sp, ep, f)
    
def h4(litterlist, h3, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h3
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h5(nn, k10, sp, ep, f)
    
def h5(litterlist, h4, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h4
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h6(nn, k10, sp, ep, f)

def h6(litterlist, h5, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h5
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h7(nn, k10, sp, ep, f)
    
def h7(litterlist, h6, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h6
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h8(nn, k10, sp, ep, f)
    
def h8(litterlist, h7, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h7
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h9(nn, k10, sp, ep, f)
    
def h9(litterlist, h8, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h8
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue
                                                elif sp >= len(k10):
                                                    h10(nn, k10, sp, ep, f)
    
def h10(litterlist, h9, startpoint, endpoint, fileproc):
    nn = list(litterlist)
    sp = int(startpoint)
    ep = int(endpoint)
    f = fileproc
    for l1 in nn:
        k1 = h9
        if ep == len(k1):
            f.write(k1 + '\n')
            continue
        elif sp >= len(k1):
            f.write(k1 + '\n')
            for l2 in nn:
                k2 = k1 + l2
                if ep == len(k2):
                    f.write(k2 + '\n')
                    continue
                elif sp >= len(k2):
                    f.write(k2 + '\n')
                for l3 in nn:
                   k3 = l2 + l3
                   if ep == len(k3):
                        f.write(k3 + '\n')
                        continue
                   elif sp >= len(k3):
                        f.write(k3 + '\n')
                   for l4 in nn:
                        k4 = k3 + l4
                        if ep == len(k4):
                            f.write(k4 + '\n')
                            continue
                        elif sp >= len(k4):
                            f.write(k4 + '\n')
                        for l5 in nn:
                            k5 = k4 + l5
                            if ep == len(k5):
                                f.write(k5 + '\n')
                                continue
                            elif sp >= len(k5):
                                f.write(k5 + '\n')
                            for l6 in nn:
                                k6 = k5 + l6
                                if ep == len(k6):
                                    f.write(k6 + '\n')
                                    continue
                                elif sp >= len(k6):
                                    f.write(k6 + '\n')
                                for l7 in nn:
                                    k7 = k6 + l7
                                    if ep == len(k7):
                                        f.write(k7 + '\n')
                                        continue
                                    elif sp >= len(k7):
                                        f.write(k7 + '\n')
                                    for l8 in nn:
                                        k8 = k7 + l8
                                        if ep == len(k8):
                                            f.write(k8 + '\n')
                                            continue
                                        elif sp >= len(k8):
                                            f.write(k8 + '\n')
                                        for l9 in nn:
                                            k9 = k8 + l9
                                            if ep == len(k9):
                                                f.write(k9 + '\n')
                                                continue
                                            elif sp >= len(k9):
                                                f.write(k9 + '\n')
                                            for l10 in nn:
                                                k10 = k9 + l10
                                                if ep == len(k10):
                                                    f.write(k10 + '\n')
                                                    continue

ch = str(input('ENC / DEC : '))
if ch == 'enc':
    w = str(input('ENTER WORD : '))
    h = str(input('ENTER HASH : '))
    if h == 'rsa' or h == 'aes':
        print()
    else:
        print()
elif ch == 'dec':
    c = str(input('ENTER CIPHER : '))
    h = str(input('ENTER HASH : '))
    if h == 'rsa' or h == 'aes' or h == 'base64':
        print()
    else:
        print()
else:
    q = str(input('DO YOU WANT TO GENERATE A WORD LIST ? '))
    if q == 'y':
        q = str(input('ENTER TYPE : '))
        if q == 'a':
            nn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 
                  'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 
                  'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 
                  'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 
                  't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y',
                  'z', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                  '-', '_', '=', '+', '|', '"', ';', ':', '/', '?', ',', '<', 
                  '>', '.', '[', ']', '{', '}', '`', '~']
        elif q == 'n':
            nn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        elif q == 'l':
            nn = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 
                  'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 
                  'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 
                  't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y','z', 'Z']
        elif q == 's':
            nn = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                  '-', '_', '=', '+', '|', '"', ';', ':', '/', '?', ',', '<', 
                  '>', '.', '[', ']', '{', '}', '`', '~']
        elif q == 'nl':
            nn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 
                  'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 
                  'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 
                  'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 
                  't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y',
                  'z', 'Z']
        elif q == 'sl':
            nn = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 
                  'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 
                  'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 
                  't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y',
                  'z', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                  '-', '_', '=', '+', '|', '"', ';', ':', '/', '?', ',', '<', 
                  '>', '.', '[', ']', '{', '}', '`', '~']
        elif q == 'ns':
            nn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                  '-', '_', '=', '+', '|', '"', ';', ':', '/', '?', ',', '<', 
                  '>', '.', '[', ']', '{', '}', '`', '~']
    else:
        sys.exit(0)