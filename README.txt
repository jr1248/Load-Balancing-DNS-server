0.
Audri Yoon          soojinyo
Jennifer Rodriguez  jr1248
1. We implemented LS and tracking by 
2. 
3. We initially had an issue with LS sometimes stalling because TS1 and TS2 were able to send their responses simultaneously.
We remedied this by having TS1 send their response first and setting a time limit before letting TS2 send its response. 
4. We learned how to implement a server that also acts as a client (LS) and have it query two simple DNS servers simultaneously.