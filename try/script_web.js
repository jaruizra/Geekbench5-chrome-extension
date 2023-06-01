import { spawn } from 'child_process';

const page_url = window.location.href;
const python_process = spawn('python', ['./geekbench5.py', page_url]);

python_process.stdout.on('data', (confirmation) => {
    console.log('okkkkk', confirmation.toString());
});