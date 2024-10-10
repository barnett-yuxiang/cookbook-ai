// funtion to get only hour from datetime string
function getHour(datetime) {
    return datetime.split(' ')[1].split(':')[0];
}

// function to impl md5 verify
function md5Verify(data, hash) {
    return md5(data) === hash;
}
