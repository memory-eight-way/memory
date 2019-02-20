#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 複数形 ing などの単語をまとめてない
# 名詞も小文字に変換している
# Mr. 等をmrに変換している

import os

def word_trans_one(w_word):
    """
    単語の標準化
    """
    tmp_word = w_word.strip()
    tmp_word = tmp_word.lower()
    
    if tmp_word.endswith(("." 
            ,"," 
            ,'"'
            ,"'"
            ,";"
            ,"!"
            ,"?"
            ,")"
            ,":",)):
        tmp_word=tmp_word[:-1]

    if tmp_word.startswith(("." 
            ,"," 
            ,'"'
            ,"'"
            ,";"
            ,"!"
            ,"?"
            ,"("
            ,":",)):
        tmp_word=tmp_word[1:]

    if tmp_word.endswith(":--"):
        tmp_word=tmp_word[:-3]

    if tmp_word.endswith("--"):
        tmp_word=tmp_word[:-2]

    if tmp_word.endswith("'s"):
        tmp_word=tmp_word[:-2]

        
    return tmp_word

def word_trans(w_word):
    pre_word=w_word
    tmp_word=word_trans_one(w_word)
    while(tmp_word!=pre_word):
        pre_word=tmp_word
        tmp_word=word_trans_one(tmp_word)
    return tmp_word
    
    
def isSkipWord(tmp_word):
    if tmp_word.strip()=="":
        return True
    if str.isdigit(tmp_word):
        return True
    if "-" in tmp_word:
        wSep=tmp_word.split("-")
        for wEle in wSep:
            if str.isdigit(wEle):
                return True
    return False

def make_word_list_fn(fn):
    """
    fn:ファイル名
    単語と使用数を辞書で返す
    """
    di_word=dict()
    f=open(fn)
    print("open:",fn)
    lines=f.readlines()
    for l in lines:
        words=l.split(" ")
        # print(words)
        for tmp_word in words:
            w_reg_word = word_trans(tmp_word)
            if isSkipWord(w_reg_word):
                #print("skip:",w_reg_word)
                continue
            if w_reg_word not in di_word:
                di_word[w_reg_word]=0
            di_word[w_reg_word]=di_word[w_reg_word]+1
            
            
    return di_word

def make_book_summary_dict(di_fn):
    """
        di_fn:辞書[ファイル名->辞書[単語→数]]
        辞書[単語→数]を返す
    """

    di_all_words =dict()
    for fn in di_fn:
        print("fn=",fn)
        tmp_wordDict=di_fn[fn]
        for tmp_word in tmp_wordDict:
            if tmp_word not in di_all_words:
                di_all_words[tmp_word]=0
            if tmp_word=="grudges":
                print("check:",tmp_word,di_all_words[tmp_word]) 
                print("check:",tmp_word,tmp_wordDict[tmp_word]) 
            di_all_words[tmp_word]=di_all_words[tmp_word]+tmp_wordDict[tmp_word]
    return di_all_words
    

def print_sum_by_chap(di_fn,chap_title):
    
    
    di_all_words =make_summary_dict(di_fn)

    di_order=dict()
    for w_word in di_all_words:
        w_count=di_all_words[w_word]
        if w_count not in di_order:
            di_order[w_count]=list()
        di_order[w_count].append(w_word)
    
    disp_key=di_order.keys()
    sorted_disp_key=sorted(disp_key,reverse=True)
    
    fn_keys=di_fn.keys()
    for fn in fn_keys:
        print ("word",",",end="")
        print(fn,",",end="")
        print()

    
    for w_count in sorted_disp_key:
        for w_word in di_order[w_count]:
            
            print(w_word,",",end="")
            for fn in fn_keys:
                if w_word in di_fn[fn]:
                    wChapCount=di_fn[fn][w_word]
                else:
                    wChapCount=0
                print(wChapCount,",",end="")
            print(di_all_words[w_word])


def make_chap_word_chap_text(di_chap_words):
    """
        章の単語辞書を作成
        単語、数を使用頻度が高いものから並べる
    """
    lines=""
    
    
    di_order=dict()
    for w_word in di_chap_words:
        w_count=di_chap_words[w_word]
        if w_count not in di_order:
            di_order[w_count]=list()
        di_order[w_count].append(w_word)
    
    disp_key=di_order.keys()
    sorted_disp_key=sorted(disp_key,reverse=True)
    #sorted_disp_key=sorted(disp_key)
    for w_count in sorted_disp_key:
        for w_word in di_order[w_count]:
            lines= lines + w_word+","+str(di_chap_words[w_word])+"\n"

    return lines


def make_chap_word_book_text(di_book_words):
    """
        本の単語辞書を作成
        単語、数を使用頻度が高いものから並べる
        章が横軸に割り込む
    """
    lines=""
    #本の章毎の辞書から本の辞書に変換    
    di_book_dict=dict()
    for w_chap in di_book_words:
        w_chap_dict=di_book_words[w_chap]
        for w_word in w_chap_dict:
            w_count=w_chap_dict[w_word]
            if w_word not in di_book_dict:
                di_book_dict[w_word]=0
            di_book_dict[w_word]=di_book_dict[w_word]+w_count
    
    
    di_order=dict()
    for w_word in di_book_dict:
        w_count=di_book_dict[w_word]
        if w_count not in di_order:
            di_order[w_count]=list()
        di_order[w_count].append(w_word )
    
    li_chap=di_book_words.keys()
    li_chap=sorted(li_chap)
    
    lines= lines+ "word,allcount"
    for w_chap in li_chap:
        lines= lines+ ","+w_chap
    lines= lines+"\n"

    disp_key=di_order.keys()
    sorted_disp_key=sorted(disp_key,reverse=True)
    #sorted_disp_key=sorted(disp_key)
    for w_count in sorted_disp_key:
        #単語の使用頻度
        #print("di_order[w_count]:",di_order[w_count])
        
        for w_word in di_order[w_count]:
            #print("wList:",w_word)
            lines= lines+ w_word+","+str(w_count)
            for w_chap in li_chap:
                #di_book_words[w_word]
                di_chap=di_book_words[w_chap]
                if w_word in di_chap:
                    lines = lines +"," + str(di_chap[w_word])
                else:
                    lines = lines+ ",0"
                  
            lines = lines+"\n"
    return lines
    
def make_chap_word_all_text(di_all_words):
    lines=""
    
    #print("di_all_words",di_all_words)
    
    di_all_dict=dict()
    for w_book_name in di_all_words:
        di_book_word=di_all_words[w_book_name]
        for w_word in di_book_word:
            w_count = di_book_word[w_word]
            if w_word not in di_all_dict:
                di_all_dict[w_word]=0
            di_all_dict[w_word] =di_all_dict[w_word]+w_count 
    
    di_order=dict()
    for w_word in di_all_dict:
        w_count = di_all_dict[w_word]
        if w_count  not in di_order:
            di_order[w_count]=list()
        if w_word not in di_order[w_count]:
            di_order[w_count].append(w_word)
    
    title_key=di_all_words.keys()
    title_key=sorted(title_key)

    lines= lines+ "word,allcount"
    for w_book_title in title_key:
        lines= lines+ ","+w_book_title
    lines= lines+"\n"

    disp_key=di_order.keys()
    sorted_disp_key=sorted(disp_key,reverse=True)
    #sorted_disp_key=sorted(disp_key)
    for w_count in sorted_disp_key:
        for w_word in di_order[w_count]:
            lines = lines+ w_word
            cnt_word=0
            info_book=""
            for w_title in title_key:
            
                w_book_dict=di_all_words[w_title]
                if w_word in w_book_dict:
                    info_book = info_book+ ","+str(w_book_dict[w_word])
                    cnt_word=cnt_word+w_book_dict[w_word]
                else:
                    info_book = info_book + ",0"
            lines=lines+","+str(cnt_word)+info_book+ "\n"
            
    return lines

    
def write_summary_chap_list(di_chap,fn_part):
    """
    ファイル単位（章）の単語リスト
    """
    # F:\practice\base\wordlist
    f=open("chap-"+fn_part+"-wordlist.csv","w")
    tmp_text=make_chap_word_chap_text(di_chap)
    f.write(tmp_text)
    f.close()

def write_summary_book_list(di_book,fn_part):
    """
    フォルダ単位（ブック）の単語リスト
    """
    f=open("book-"+fn_part+"-wordlist.csv","w")
    tmp_text=make_chap_word_book_text(di_book)
    f.write(tmp_text)
    f.close()
    
    
def write_summary_all_list(di_all_words):    
    """
    全体の単語リスト
    """
    f=open("all-book-wordlist.csv","w")
    #print ("di_all_words",di_all_words)
    tmp_text=make_chap_word_all_text(di_all_words)
    f.write(tmp_text)
    f.close()
    
    
    
def print_word_chap(di_fn):
    di_book_words =make_book_summary_dict(di_fn)
    txt_chap=make_chap_word_chap_text(di_book_words)

def print_word_book(di_fn):
    di_book_words =make_book_summary_dict(di_fn)
    txt_book=make_chap_word_chap_text(di_book_words)

def print_word_all(di_all_words):
    di_book_words =make_book_summary_dict(di_fn)
    txt_all=make_chap_word_chap_text(di_book_words)
    
def make_word_list(w_dir_root,w_file_suffix):
    """
    フォルダの単語リストを作成
    """
    di_book=dict()
    wfiles=os.listdir(w_dir_root)
    chap_title=list()
    for w_chap_file_name in wfiles:
        print("parse file:",w_chap_file_name )
        chap_title.append(w_chap_file_name)
        di_book[w_chap_file_name]=make_word_list_fn(os.path.join(w_dir_root,w_chap_file_name))
        #write_summary_chap_list(di_book[w_chap_file_name ],w_file_suffix+w_chap_file_name )
        
        
    #write_summary_book_list(di_book,w_file_suffix)
    return di_book
    
    
def update_di_all(di_all, di_book,w_book_name):
    if w_book_name not in di_all:
        di_all[w_book_name]=dict()
        
    for w_chap in di_book:
        print("w_chap:",w_chap )
        di_chap=di_book[w_chap]
        di_tmp_book=di_all[w_book_name]
        for w_word in di_chap:
            #print("w_word:",w_word)
            if w_word not in di_tmp_book:
                di_tmp_book[w_word]=0
            di_tmp_book[w_word]=di_tmp_book[w_word]+di_chap[w_word]
    
def make_word_list_making():
    di_all = dict()

    di_book=make_word_list("../TheArtOfWar","TheArtOfWar")
    update_di_all(di_all, di_book ,"TheArtOfWar")

    di_book=make_word_list("../holmes/SH_01_A_Study_in_Scarlet","SH_01")
    update_di_all(di_all, di_book,"SH_01" )

    di_book=make_word_list("../holmes/SH_02_The_Sign_of_the_Four","SH_02")
    update_di_all(di_all, di_book,"SH_02" )

    write_summary_all_list(di_all)

def make_word_list_main():
    di_all = dict()

    di_book=make_word_list("../TheArtOfWar/base","TheArtOfWar")
    update_di_all(di_all, di_book ,"TheArtOfWar")

    di_book=make_word_list("../holmes/base/SH_01_A_Study_in_Scarlet","SH_01")
    update_di_all(di_all, di_book,"SH_01" )

    di_book=make_word_list("../holmes/base/SH_02_The_Sign_of_the_Four","SH_02")
    update_di_all(di_all, di_book,"SH_02" )

    di_book=make_word_list("../holmes/base/SH_03_The_Hound_of_the_Baskervilles","SH_03")
    update_di_all(di_all, di_book ,"SH_03" )

    di_book=make_word_list("../holmes/base/SH_04_The_Valley_of_Fear","SH_04")
    update_di_all(di_all, di_book  ,"SH_04")

    di_book=make_word_list("../holmes/base/SH_05_The_Adventures_of_Sherlock_Holmes","SH_05")
    update_di_all(di_all, di_book  ,"SH_05")

    di_book=make_word_list("../holmes/base/SH_06_The_Memoirs_of_Sherlock_Holmes","SH_06")
    update_di_all(di_all, di_book  ,"SH_06")

    di_book=make_word_list("../holmes/base/SH_07_The_Return_of_Sherlock_Holmes","SH_07")
    update_di_all(di_all, di_book  ,"SH_07")

    di_book=make_word_list("../holmes/base/SH_08_His_Last_Bow","SH_08")
    update_di_all(di_all, di_book  ,"SH_08")
    
    # make_word_list("../holmes/SH_09_The_Case-Book_of_Sherlock_Holmes","SH_09")

    write_summary_all_list(di_all)

if __name__=="__main__":
    make_word_list_main()
    #make_word_list_making()





    
    
    