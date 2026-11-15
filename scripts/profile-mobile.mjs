import {chromium} from 'playwright';
import {spawn} from 'node:child_process';
import fs from 'node:fs';
const server=spawn('python3',['-m','http.server','8873'],{stdio:'ignore'});
const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
try{
 const page=await browser.newPage({viewport:{width:390,height:844},isMobile:true,deviceScaleFactor:1});
 await page.route(/https:\/\/(fonts|cdnjs)/,r=>r.abort());
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const cdp=await page.context().newCDPSession(page);await cdp.send('Emulation.setCPUThrottlingRate',{rate:6});
 await page.goto(process.env.URL||'http://localhost:8873');
 await page.waitForFunction(()=>window.state&&Object.keys(state.vocabDB).length&&document.querySelector('#home-lesson-grid')?.children.length,{timeout:120000});
 console.log('ready',await page.evaluate(()=>({now:performance.now(),words:Object.values(state.vocabDB).flat().length,stats:Object.keys(state.stats).length})));
 await page.evaluate(()=>{const words=Object.values(state.vocabDB).flat();state.stats={};for(const w of words.slice(0,300)){for(const suffix of ['',':kana'])state.stats['V:'+w.id+suffix]={nextDue:1,correct:2,reps:2,weight:1,interval:1};}for(const k of Object.keys(state.kanjiDB).slice(0,200))state.stats['K:'+k]={nextDue:1,reps:1};});
 const results={};
 async function bench(label,fn){results[label]=[];for(let i=0;i<3;i++){results[label].push(await page.evaluate(async src=>{const t=performance.now();await (0,eval)(src);return Math.round(performance.now()-t)},fn));}console.log(label,results[label]);}
 await cdp.send('Profiler.enable');await cdp.send('Profiler.start');
 await bench('home',"showView('home')");
 await bench('reviewB',"setHomeReviewPart('B')");await bench('reviewBoth',"setHomeReviewPart('both')");
 await bench('reviewGrid',"toggleHomeReviewGrid()");
 await bench('vocab',"showView('vocab')");await bench('kanji',"showView('kanji')");await bench('grammar',"showView('grammar')");await bench('reading',"showView('reading')");await bench('tests',"showView('test')");
 const profile=await cdp.send('Profiler.stop');fs.writeFileSync('/tmp/n3-'+(process.env.LABEL||'before')+'.cpuprofile',JSON.stringify(profile.profile));
 console.log('errors',errors);fs.writeFileSync('/tmp/n3-'+(process.env.LABEL||'before')+'.json',JSON.stringify({results,errors},null,2));
 await page.evaluate(()=>showView('home'));await page.screenshot({path:'/tmp/n3-'+(process.env.LABEL||'before')+'.png',fullPage:true});
}finally{await browser.close();server.kill();}
