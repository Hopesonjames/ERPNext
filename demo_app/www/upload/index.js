
$('#upload-form').submit(e=>{
   e.preventDefault();
   // upload method
   console.log(e.target)
})


let makecall = async()=>{
    let formdata = $('#upload-form').serializeArray()
}

let imagefile = new FormData();
imagefile.append('file_url',
'https://cdn.dribbble.com/users/8092133/screenshots/15780797/media/ac26b011c5894f99d0e93d18b2d98052.jpg');
imagefile.append('doctype','Student');
imagefile.append('docname','6767')
fetch('/api/method/upload_file', {
    headers: {
        'X-Frappe-CSRF-Token': frappe.csrf_token
    },
    method: 'POST',
    body: imagefile

})
. then(res=>res.json())