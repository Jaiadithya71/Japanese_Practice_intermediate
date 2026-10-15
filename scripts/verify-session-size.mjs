import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const source = fs.readFileSync('js/home.js', 'utf8');
const body = source.match(/function homeRunSize\(\) \{[\s\S]*?\n\}/)[0];
function check(initial, expected) {
  const data = new Map(Object.entries(initial));
  const context = vm.createContext({localStorage: {getItem: k => data.get(k) ?? null, setItem: (k,v) => data.set(k,v)}});
  vm.runInContext(body, context);
  assert.equal(vm.runInContext('homeRunSize()', context), expected);
  return {data,context};
}
check({}, 'all');
check({n3_home_session_size:'20'}, 'all');
check({n3_home_session_size:'50', n3_home_session_size_default_v2:'all'}, '50');
check({n3_home_session_size:'bad', n3_home_session_size_default_v2:'all'}, 'all');
const c = vm.createContext({localStorage:{getItem:()=>{throw Error('denied')}}});
vm.runInContext(body,c);
assert.equal(vm.runInContext('homeRunSize()',c),'all');
assert.match(fs.readFileSync('index.html','utf8'), /value="all" selected>All words/);
console.log('All session default: fresh device, existing 20-word migration, saved later choice, invalid value and unavailable storage passed.');
