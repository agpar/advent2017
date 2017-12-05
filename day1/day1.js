var count_consecutive_digits = function(digit_string) 
{
	var digit_list = digit_string.split('').map(x => parseInt(x, 10));
	var result = 0;
	for(var i = 0; i < digit_list.length - 1; i++) 
	{
		if(digit_list[i] == digit_list[i + 1]) {
			result += digit_list[i];
		}
	}
	if(digit_list[digit_list.length - 1] == digit_list[0]) {
		result += digit_list[digit_list.length - 1];
	}
	return result;
}