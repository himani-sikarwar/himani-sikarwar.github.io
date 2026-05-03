import re
import csv
import time
import requests
import html
from pybtex.database import parse_string

# -----------------------------
# INPUT: Your BibTeX data
# -----------------------------
bib_data = """@inproceedings{sikarwar2020labvs,
  title={LABVS: Lightweight authentication and batch verification scheme for universal internet of vehicles (UIoV)},
  author={Sikarwar, Himani and Nahar, Ankur and Das, Debasis},
  booktitle={2020 IEEE 91st Vehicular Technology Conference (VTC2020-Spring)},
  pages={1--6},
  year={2020},
  organization={IEEE}
}

@inproceedings{sikarwar2022eecaap,
  title={EECAAP: Efficient Edge-Computing based Anonymous Authentication Protocol for IoV},
  author={Sikarwar, Himani and Das, Debasis},
  booktitle={2022 IEEE 29th International Conference on High Performance Computing, Data, and Analytics (HiPC)},
  pages={302--307},
  year={2022},
  organization={IEEE}
}

@article{sikarwar2023novel,
  title={A novel MAC-based authentication scheme (NoMAS) for Internet of Vehicles (IoV)},
  author={Sikarwar, Himani and Das, Debasis},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  volume={24},
  number={5},
  pages={4904--4916},
  year={2023},
  publisher={IEEE}
}

@inproceedings{nahar2023cachein,
  title={Cachein: A secure distributed multi-layer mobility-assisted edge intelligence based caching for internet of vehicles},
  author={Nahar, Ankur and Sikarwar, Himani and Jain, Sanyam and Das, Debasis},
  booktitle={2023 IEEE/ACM 23rd International Symposium on Cluster, Cloud and Internet Computing (CCGrid)},
  pages={437--446},
  year={2023},
  organization={IEEE}
}

@inproceedings{nahar2020csbr,
  title={CSBR: A cosine similarity based selective broadcast routing protocol for vehicular ad-hoc networks},
  author={Nahar, Ankur and Sikarwar, Himani and Das, Debasis},
  booktitle={2020 ifip networking conference (networking)},
  pages={404--412},
  year={2020},
  organization={IEEE}
}

@article{sikarwar2024secure,
  title={Secure: Secure and efficient protocol using randomness and edge-computing for drone-assisted internet of vehicles},
  author={Sikarwar, Himani and Vasudev, Harsha and Das, Debasis and Conti, Mauro and Mondal, Koustav Kumar},
  journal={IEEE Transactions on Network and Service Management},
  volume={21},
  number={6},
  pages={6974--6988},
  year={2024},
  publisher={IEEE}
}

@article{nahar2025mrmh,
  title={MRMH: Multi-Constraint Routing Optimization Using Hybrid Metaheuristics in Vehicular Ad-Hoc Networks},
  author={Nahar, Ankur and Sikarwar, Himani and Das, Debasis and Misra, Sudip},
  journal={IEEE Transactions on Network Science and Engineering},
  year={2025},
  publisher={IEEE}
}

@inproceedings{sikarwar2022laas,
  title={LAAS: lightweight anonymous authentication scheme for universal internet of vehicles (UIOV)},
  author={Sikarwar, Himani and Nahar, Ankur and Das, Debasis},
  booktitle={2022 International Wireless Communications and Mobile Computing (IWCMC)},
  pages={859--864},
  year={2022},
  organization={IEEE}
}

@article{sikarwar2023secedge,
  title={SecEdge: Secure edge-computing-based hybrid approach for data collection and searching in IoV},
  author={Sikarwar, Himani and Das, Debasis},
  journal={IEEE Transactions on Network and Service Management},
  volume={21},
  number={1},
  pages={1213--1225},
  year={2023},
  publisher={IEEE}
}

@inproceedings{sikarwar2020efficient,
  title={An Efficient Lightweight Authentication and Batch Verification Scheme for Universal Internet of Vehicles (UIoV)},
  author={Sikarwar, Himani and Das, Debasis},
  booktitle={2020 International Wireless Communications and Mobile Computing (IWCMC)},
  pages={1266--1271},
  year={2020},
  organization={IEEE}
}

@inproceedings{sikarwar2020efficientblockchain,
  title={Efficient authentication scheme using blockchain in IoT devices},
  author={Sikarwar, Himani and Das, Debasis and Kalra, Sumit},
  booktitle={International Conference on Advanced Information Networking and Applications},
  pages={630--641},
  year={2020},
  organization={Springer}
}

@inproceedings{sikarwar2023smmap,
  title={SMMAP: Secure MAC-based Mutual Authentication Protocol for IoV},
  author={Sikarwar, Himani and Das, Debasis},
  booktitle={Proceedings of the 24th International Conference on Distributed Computing and Networking},
  pages={330--335},
  year={2023}
}

@inproceedings{nahar2022alcfier,
  title={AlcFier: Adaptive self-learning classifier for routing in vehicular ad-hoc network},
  author={Nahar, Ankur and Sikarwar, Himani and Das, Debasis},
  booktitle={2022 IEEE 47th conference on local computer networks (LCN)},
  pages={311--314},
  year={2022},
  organization={IEEE}
}

@article{sikarwar2021towards,
  title={Towards lightweight authentication and batch verification scheme in IoV},
  author={Sikarwar, Himani and Das, Debasis},
  journal={IEEE Transactions on Dependable and Secure Computing},
  volume={19},
  number={5},
  pages={3244--3256},
  year={2021},
  publisher={IEEE}
}

@inproceedings{sikarwar2020lightweight,
  title={A lightweight and secure authentication protocol for WSN},
  author={Sikarwar, Himani and Das, Debasis},
  booktitle={2020 International Wireless Communications and Mobile Computing (IWCMC)},
  pages={475--480},
  year={2020},
  organization={IEEE}
}

@article{sikarwar2025dybatch,
  title={DyBatch: Message Prioritization and Priority-driven Dynamic Batch Verification in Large-scale IoV Networks},
  author={Sikarwar, Himani and Nahar, Ankur and Das, Debasis},
  journal={IEEE Transactions on Vehicular Technology},
  year={2025},
  publisher={IEEE}
}

@article{mondal2025secure,
  title={Secure IoT Communications with Optimized AES and Dynamic Threat Modeling on Embedded System},
  author={Mondal, Koustav Kumar and Sikarwar, Himani and Das, Debasis and Fan, Chun-I},
  journal={IEEE Transactions on Consumer Electronics},
  year={2025},
  publisher={IEEE}
}
"""

# -----------------------------
# Helper Functions
# -----------------------------

def generate_slug(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


def clean_abstract(raw_abstract):
    if not raw_abstract:
        return ""

    decoded = html.unescape(raw_abstract)
    cleaned = re.sub(r'<[^>]+>', '', decoded)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    return cleaned


def get_crossref_data(title):
    try:
        url = f"https://api.crossref.org/works?query.title={title}"
        response = requests.get(url, timeout=10).json()

        if response.get('message', {}).get('items'):
            item = response['message']['items'][0]

            doi = item.get("DOI", "")
            paper_url = item.get("URL", "")
            raw_abstract = item.get("abstract", "")

            abstract = clean_abstract(raw_abstract)

            return doi, paper_url, abstract

    except Exception as e:
        print(f"Crossref error for '{title}': {e}")

    return "", "", ""


def get_openalex_citations(title):
    try:
        url = f"https://api.openalex.org/works?search={title}"
        response = requests.get(url, timeout=10).json()

        if response.get('results'):
            return response['results'][0].get('cited_by_count', 0)

    except Exception as e:
        print(f"OpenAlex citation error for '{title}': {e}")

    return 0


def get_openalex_abstract(title):
    try:
        url = f"https://api.openalex.org/works?search={title}"
        data = requests.get(url, timeout=10).json()

        if data.get('results'):
            inv_index = data['results'][0].get('abstract_inverted_index')

            if inv_index:
                words = []
                for word, positions in inv_index.items():
                    for pos in positions:
                        words.append((pos, word))

                words.sort()
                return " ".join([w for _, w in words])

    except Exception as e:
        print(f"OpenAlex abstract error for '{title}': {e}")

    return ""


# -----------------------------
# MAIN PIPELINE
# -----------------------------

parsed = parse_string(bib_data, 'bibtex')
output_rows = []

for key, entry in parsed.entries.items():
    title = entry.fields.get('title', '')
    year = entry.fields.get('year', '')
    venue = entry.fields.get('booktitle', '')
    category = entry.type

    print(f"\nProcessing: {title}")

    # Crossref
    doi, paper_url, abstract = get_crossref_data(title)

    # Fallback to OpenAlex abstract
    if not abstract:
        abstract = get_openalex_abstract(title)

    # Final fallback
    if not abstract:
        abstract = "Abstract not available"

    # OpenAlex citations
    citation = get_openalex_citations(title)

    # Slug
    slug = generate_slug(title)

    # Static slides URL
    slides_url = "https://your-static-slides-link.com"

    # Row
    row = {
        "pub_date": year,
        "title": title,
        "venue": venue,
        "excerpt": abstract[:300],
        "citation": citation,
        "url_slug": slug,
        "paper_url": paper_url,
        "slides_url": slides_url,
        "category": category
    }

    output_rows.append(row)

    # Rate limiting
    time.sleep(1)

# -----------------------------
# SAVE TO CSV
# -----------------------------

output_file = "publications.csv"

if output_rows:
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"\n✅ CSV generated: {output_file}")

    # Preview
    with open(output_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
else:
    print("⚠️ No data to write.")
