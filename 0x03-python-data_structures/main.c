#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>




int main(int argc , char ** argv)
{
        int fd;
        size_t len;
        size_t size = 0;

	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
		return (-1);
	}
        if (!argv[1])
                return (-1);

        fd = open(argv[1], O_CREAT | O_WRONLY | O_APPEND, 0777);
        if (fd == -1)
                return (-1);
	
	const char *text_content = "#!/usr/bin/python3";

        len = strlen(text_content);
        if (len)
                size = write(fd, text_content, len);

        close(fd);
        return (0);
}
