"""this script uses the vt-py library to interact with virustotal before using this script make sure you installed the library in your environemnt by simply run the command 
python -m pip install vt-py"""
import vt,json
def hash_intel_vt(client,hash):
    """take a vt.Client object and a filehash "string" and returns the last_analysis_stats for that hash"""
    parameters={'query':hash}
    filehashReport=""
    try:
        hashReport=client.iterator("/search",params=parameters)
        for i in hashReport:
            stats=i.get("last_analysis_stats")
            filehashReport+="VirusTotal filehash analysis: filehash is reported as harmless by ({}), type unsupported by ({}), suspicious by ({}),  malicious by ({}) and undected by ({})\n"\
                .format(*[stats.get(key) for key in ["harmless","type-unsupported","suspicious","malicious","undetected"]])
        if len(filehashReport)==0:
            filehashReport="VirusTotal doesn't have information available for that filehash !!\n"
    except Exception as e:
        filehashReport="an error {} occured while trying to query VT for the filehash !!".format(e)
    return filehashReport 

# import nest_asyncio
# nest_asyncio.apply()
#uncommment the previous 2 lines if you are running this code from jupyter notebook and having issue an error This event loop is already running
# replace your vt api key with your key and leave the quotes you will find your virus total api key by clicking on your profile and going to API key
VT_api_key="your vt api key"

vtClient=vt.Client(VT_api_key)

hashes=list(set([x.strip() for x in (input("Enter file hash or multiple file hashes with comma separated: ")).split(',')]))

print('\n')
for filehash in hashes:
    print(filehash+":\n"+hash_intel_vt(vtClient,filehash)+'\n')
    

