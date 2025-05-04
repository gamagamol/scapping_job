import scrapy


class BehavoxSpiderSpider(scrapy.Spider):
    name = "behavox_spider"
    allowed_domains = ["job-boards.greenhouse.io"]
    start_urls = ["https://job-boards.greenhouse.io/behavox"]

    def parse(self, response):
        all_jobs = []
        jobs_per_dep = response.css(".job-posts--table--department")
        for job_per_dept in jobs_per_dep:
            dep = job_per_dept.css(".job-posts--department-path p::text").get()
            sub_dep = job_per_dept.css(".section-header.font-primary::text").get()
            jobs=job_per_dept.css(".job-posts--table table tbody tr.job-post")

            for job in jobs:
                job_link=job.css("a::attr(href)").get()
                job_name = job.css("a .body.body--medium::text").get()
                job_location = job.css("a .body.body__secondary.body--metadata::text").get()
                
                job_data = {
                    'department': dep,
                    'sub_department': sub_dep,
                    'job_link': job_link,
                    'job_name': job_name,
                    'job_location': job_location
                }
                
                all_jobs.append(job_data)
                
        return all_jobs
            
        
        
