#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseフォルダのファイルを加工して問題に変換する
"""
    AesopFable のテキストを記憶術用のテキストに変換するサンプルです。
    
    __SEP_TITLE__
        上記文字列で区切ったテキストの1行目をタイトルとします
        それ以下の行を本文としてます。

    処理的には
        一度、改行を空白に置き換え→改行と思われる場所で改行
        を行います。
        
    テキスト自体を変更したり、テキスト毎に改行しない処理とかで、微調整を入れます。
    どうしてもムリなときは手作業でテキストを作ります。
    
"""
import os
import random

def reg_sybmol(wstr):
    """
        テキスト内の2バイト文字を1バイトの文字に置き換え
        テキストを打ち込んで確認する際に1バイトの文字の方が楽            
    """
    wstr=wstr.replace("”",'"')
    wstr=wstr.replace("“",'"')
    wstr=wstr.replace("’","'")
    return wstr
    
    
def makedirs(dir_make):
    up_dir_make = os.path.abspath(dir_make).upper()
    if os.path.isdir(dir_make):
        return
    return os.makedirs(dir_make)

def parse_text(li_line):
    """
    テキストを解析して
        タイトル、本文
        のリストにして返す
    """
    li_ret=list()
    w_block_list=list()
    w_new_block=False
    w_title=None
    w_parsing=False
    for line in li_line:
        if line.strip()=="":
            continue
        if "__SEP_TITLE__"==line.strip():
            #新しいブロックの開始
            w_new_block=True
            li_ret.append([w_title,w_block_list])
            w_block_list=list()
            w_parsing=True
        else:
            if w_new_block:
                #新規のブロック　タイトル行を取得
                w_title=reg_sybmol(line.strip())
                print("w_title:",w_title)
                w_new_block=False
            else:
                if w_parsing:
                    w_block_list.append(reg_sybmol(line.strip()))
    
    li_ret.append((w_title,w_block_list))
        
    return li_ret

def get_sub_dir_name(w_cnt):
    w_cnt=int((w_cnt-1) / 10)  +1 
    w_numstr=str(w_cnt)
    w_numstr="0"*(2-len(w_numstr))+w_numstr
    
    return "AF-"+w_numstr

def get_fn_num000(w_cnt):
    w_numstr=str(w_cnt)
    w_numstr="0"*(3-len(w_numstr))+w_numstr
    return w_numstr

def title_to_fn(wstr):
    """
    タイトルの文字列をフォルダ用に変換
        記号を_にする
    """
    
    wstr=wstr.replace(" ","_")            
    wstr=wstr.replace("'","_")            
    wstr=wstr.replace(",","_")            
    wstr=wstr.replace(".","_")            
    wstr=wstr.replace("-","_")            
    return wstr
    

UPPER_A_Z=[chr(i) for i in range(65, 65+26)] # A,B

def suppress_new_line(wstr,wsuppress):
    return wstr.replace(wsuppress, wsuppress.replace("__NEW_LINE__"," "))

def block_to_mnemonic(li_text_block):

    # 改行を空白に置き換え
    w_str=" ".join(li_text_block)
    
    # ピリオド、?、! ＋空白は改行に置き換え
    for ch in [".","?","!"]:
        w_str=w_str.replace(ch+" ", ch+"__NEW_LINE__")
    
    # ' + 空白 + 大文字　は空白を改行に置き換え
    # " + 空白 + 大文字　は空白を改行に置き換え
    for ch in UPPER_A_Z:
        w_str=w_str.replace('" '+ ch, '"__NEW_LINE__'+ch)
        w_str=w_str.replace("' "+ ch, "'__NEW_LINE__"+ch)
    
    w_str=w_str.replace('" "','"__NEW_LINE__"')
    
    #改行の抑制
    
    w_str= suppress_new_line(w_str,"Frenchman,M.__NEW_LINE__Claude")
    w_str= suppress_new_line(w_str,"by M.__NEW_LINE__Mezeriac.")
    w_str= suppress_new_line(w_str,"publication of M.__NEW_LINE__Mezeriac,")
    w_str= suppress_new_line(w_str,"Professor K.__NEW_LINE__O.__NEW_LINE__Mueller")
    w_str= suppress_new_line(w_str,"1327 A.D.__NEW_LINE__he ")

    #改行で文字列を分割    
    w_tmp_li=w_str.split("__NEW_LINE__")
     
    
    #行番号の付加
    w_ret=list()
    wlinenumber=1
    for wline in w_tmp_li:
        w_ret.append(str(wlinenumber)+". " + wline+"\n")
        wlinenumber=wlinenumber+1 
    return w_ret
    
def make_base_file(fn):
    """
    記憶術用のファイルを作成
    """
    f=open(fn,"r")
    lines=f.readlines()
    f.close()
    
    
    #ファイルを読み込んでブロックに分割
    li_info=parse_text(lines)
    w_cnt=0
    for w_info in li_info:
        #ブロック単位に処理 
        if w_info[0]==None:
            continue
        print(w_cnt,":",w_info[0])
        w_cnt=w_cnt+1
       
        #保存ディレクトリ
        makedirs("./AesopFable")
        w_sub_dir=get_sub_dir_name(w_cnt)
        makedirs("./AesopFable/"+w_sub_dir)

        #保存ファイル名        
        block_fn="./AesopFable/"+w_sub_dir+"/AF-"+get_fn_num000(w_cnt)+"-"+title_to_fn(w_info[0])+".txt"
        #print(block_fn)

        #ファイルへの書き込み
        f=open(block_fn,"w")
        
        #書き込み時に　行番号＋行内容に変換
        w_mnemonic=block_to_mnemonic(w_info[1])
        w_text=w_info[0]+"\n\n"+ "\n".join(w_mnemonic)
        f.write(w_text)    
        f.close()
    

    
def main():
    make_base_file("aesop_fable.txt")
    

if __name__=="__main__":
    main()
    #print("UPPER_A_Z,",UPPER_A_Z)